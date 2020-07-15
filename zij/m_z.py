import numpy as np
import copy

from enhance_ubound import enhance_ubound


def modify_z(primary_z, primary_x, facility, demand, level, q, f, c, h1, h2, I, J, K, best_value_ubound):
	"""
	修正松弛问题的解决方案，得到上界解
	:param facility:   设施点数量
	:param primary_z:  松弛问题的分配方案
	:param primary_x:  设施建立方案
	:param q: 		   运输距离
	:param f: 		   设施建设成本
	:param c: 		   设施容量
	:return: 		   ubound [利用 z (修正后的解决方案)求得 ubound ]
	"""
	# 遍历每一个已建设施点，测试该设施点是否超量供应
	for j in range(facility):
		if primary_x[j] != 0:
			while (sum(primary_z[i, j, k] * h1[i] for i in range(demand) for k in range(level)) >= c[j]) \
				or (sum(primary_z[i, j, k] * h2[i] for i in range(demand) for k in range(level)) >= c[j]):
				real_h1 = np.zeros(demand)
				real_h2 = np.zeros(demand)

				# 根据需求编号，求出其需求量
				for i in range(demand):
					if (primary_z[i, j, 0] != 0) or (primary_z[i, j, 1] != 0):
						real_h1[i] = h1[i]
						real_h2[i] = h2[i]

				# 分别合计白天和夜晚需求量，选出总需求量最大的那一组的最大需求点编号
				if sum(real_h1) > sum(real_h2):
					belong_q1 = max(real_h1)
					index_belong_q1 = real_h1.tolist().index(belong_q1)  # 总需求最大点的编号索引
					max_demand_point = index_belong_q1
					primary_z[index_belong_q1, j, 0] = 0
					primary_z[index_belong_q1, j, 1] = 0
				else:
					belong_q2 = max(real_h2)
					index_belong_q2 = real_h2.tolist().index(belong_q2)
					max_demand_point = index_belong_q2
					primary_z[index_belong_q2, j, 0] = 0
					primary_z[index_belong_q2, j, 1] = 0

				# 第一层供应
				mody_q1 = copy.deepcopy(q[max_demand_point, :, 0])
				# for each_q1 in range(facility):
				# 	if mody_q1[each_q1] == 100:
				# 		mody_q1[each_q1] = 0
				shortest_dist1 = sorted(mody_q1)

				dem_be_meet = False
				# 依次取出能够 有效 供应最大需求点最近的设施距离和该设施点编号
				for fac_to_demand_dist in shortest_dist1:
					if fac_to_demand_dist < 100:  # 确保该设施能够覆盖能够供应
						fac_reliable = mody_q1.tolist().index(fac_to_demand_dist)

						# 判断路径最短的设施点是否已经被选中，且保证该有效供应设施点不是原设施点，也不是未建设施点
						if (fac_reliable != j) and (primary_x[fac_reliable] == 1):
							# 是否满足容量要求
							if c[fac_reliable] - sum(
									primary_z[dem, fac_reliable, ceng] * h1[dem] for dem in range(demand) for
									ceng in range(level)) >= h1[max_demand_point] and \
									c[fac_reliable] - sum(
								primary_z[dem, fac_reliable, ceng] * h2[dem] for dem in range(demand)
								for ceng in range(level)) >= h2[max_demand_point]:
								print("第{}设施点的最大需求点{}被剔除，设施点{}的剩余容量的第1层满足要求".format(j, max_demand_point, fac_reliable))
								primary_z[max_demand_point, fac_reliable, 0] = 1
								primary_z[max_demand_point, fac_reliable, 1] = 0
								dem_be_meet = True
								break

				# # 若第一层满足需求，直接结束整个循环
				# if dem_be_meet:
				# 	break

				# 第二层供应
				mody_q2 = copy.deepcopy(q[max_demand_point, :, 1])
				for each_q2 in range(facility):
					if mody_q2[each_q2] == 100:
						mody_q2[each_q2] = 0
				# shortest_dist2 = sorted(mody_q2, reverse=True)
				shortest_dist2 = sorted(mody_q2)

				if not dem_be_meet:
					for fac_to_demand_dist2 in shortest_dist2:
						if fac_to_demand_dist2 > 0:  # 确保该设施能够覆盖能够供应
							fac_reliable2 = mody_q2.tolist().index(fac_to_demand_dist2)

							# 判断路径最短的设施点是否已经被选中，且保证该有效供应设施点不是原设施点，也不是未建设施点
							if (fac_reliable2 != j) and (primary_x[fac_reliable2] == 1):
								# 是否满足容量要求
								if c[fac_reliable2] - sum(
										primary_z[dem, fac_reliable2, ceng] * h1[dem] for dem in range(demand)
										for ceng in range(level)) >= h1[max_demand_point] and c[fac_reliable2] - sum(
									primary_z[dem, fac_reliable2, ceng] * h2[dem] for dem in range(demand)
									for ceng in range(level)) >= h2[max_demand_point]:

									print("第{}设施点的最大需求点{}被剔除，设施点{}的剩余容量的第2层满足其要求".format(j, max_demand_point, fac_reliable2))
									primary_z[max_demand_point, fac_reliable2, 0] = 0
									primary_z[max_demand_point, fac_reliable2, 1] = 1
									dem_be_meet = True
									break

				# # 若第二层满足需求，直接结束整个循环
				# if dem_be_meet:
				# 	break

				if not dem_be_meet:
					for new_fac_to_demand_dist in shortest_dist1:
						new_fac = shortest_dist1.index(new_fac_to_demand_dist)
						if primary_x[new_fac] == 0:
							print("新建了编号为{}的设施点".format(new_fac))
							primary_x[new_fac] = 1
							primary_z[max_demand_point, new_fac, 0] = 1
							primary_z[max_demand_point, new_fac, 1] = 0
							break

			# 如若没用到，直接拆除
			if sum(primary_z[d, j, l] for d in range(demand) for l in range(level)) == 0 and j > 32:
				primary_x[j] = 0

	# 得到修正后的可行解
	print(">>>>>>>>>>得到修正后的可行解", primary_x)

	ubound = sum(f[j] * primary_x[j] for j in J) + sum(1 - sum(primary_z[i, j, 0] for j in J) for i in I) + \
			 sum(primary_z[i, j, k] * q[i][j][k] for i in I for j in J for k in K)

	# slack_h1 = np.zeros(facility)
	# slack_h2 = np.zeros(facility)
	# for j in J:
	# 	slack_h1[j] = sum(primary_z[i, j, k] * h1[i] for i in I for k in K) - c[j] * primary_x[j]
	# 	slack_h2[j] = sum(primary_z[i, j, k] * h2[i] for i in I for k in K) - c[j] * primary_x[j]
	#
	# print("-----------------------------------")
	# print("slack_h1", slack_h1)
	# print("slack_h2", slack_h2)
	# print("-----------------------------------")

	if ubound < best_value_ubound * 2:
		up_mdl = enhance_ubound(q, h1, h2, c, f, level, facility, demand, primary_x)
		if up_mdl.solve():
			ubound = up_mdl.objective_value

	return ubound
