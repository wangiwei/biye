from docplex.mp.model import Model


# --------------- 松弛模型 -----------
def Lagrange_relaxation_model(q, h1, h2, c, f, level, facility, demand, lambda_, mju):
	"""
	:param q: 距离函数 demand * facility * level
	:param h1: 白天需求 demand
	:param h2: 夜晚需求 demand
	:param c:  容量 facility * 25
	:param f:  建设成本 facility
	:param level: 层级 level
	:param facility:  拟建设施数
	:param demand:   需求点数
	:param lamda_:  乘子
	:param mju:     乘子
	:return:    mdl(Model实例模型)
	"""
	mdl = Model(name="facility location")
	""" 
	这是主要用来求解120急救中心布点的问题，
	使用层级设施选址模型的松弛子模型
	"""
	mdl.I = [i for i in range(demand)]
	mdl.J = [j for j in range(facility)]
	mdl.K = [k for k in range(level)]
	mdl.z = mdl.binary_var_cube(mdl.I, mdl.J, mdl.K, name='z')
	mdl.x = mdl.binary_var_list(mdl.J, name='x')

	mdl.add_constraints(
		(mdl.sum(mdl.z[i, j, k] for j in mdl.J for k in mdl.K) >= 1) for i in mdl.I)
	mdl.add_constraints((mdl.z[i, j, k] <= mdl.x[j]) for i in mdl.I for j in mdl.J for k in mdl.K)

	# 容量约束 -> 将要被松弛
	# mdl.add_constraints(
	#     (mdl.sum(z[i, j, k] * h1[i] for i in mdl.I for k in mdl.K) <= c[j] * x[j]) for j in
	#     mdl.J)
	# mdl.add_constraints(
	#     (mdl.sum(z[i, j, k] * h2[i] for i in mdl.I for k in mdl.K) <= c[j] * x[j]) for j in
	#     mdl.J)

	# 加入冗余约束
	mdl.add_constraints((mdl.sum(mdl.z[i, j, k] for k in mdl.K) <= 1) for i in mdl.I for j in mdl.J)
	mdl.add_constraints((mdl.sum(mdl.z[i, j, k] for j in mdl.J) <= 1) for i in mdl.I for k in mdl.K)

	# 目标函数
	mdl.minimize(mdl.sum(f[j] * mdl.x[j] for j in mdl.J) +
				 mdl.sum(1 - mdl.sum(mdl.z[i, j, 0] for j in mdl.J) for i in mdl.I) +
				 mdl.sum(mdl.z[i, j, k] * q[i][j][k] for i in mdl.I for j in mdl.J for k in mdl.K) +
				 mdl.sum(
					 lambda_[j] * (mdl.sum(mdl.z[i, j, k] * h1[i] for i in mdl.I for k in mdl.K) - c[j] * mdl.x[j]) +
					 mju[j] * (mdl.sum(mdl.z[i, j, k] * h2[i] for i in mdl.I for k in mdl.K) - c[j] * mdl.x[j]) for j in
					 mdl.J)
				 )

	return mdl
