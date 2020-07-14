import numpy as np


def update_lam_mjuupdate_lam_mjuupdate_lam_mju(lambda_, mju, best_value_ubound, best_value, facility, scale,
													  primary_z, primary_x, I, J, K, h1, h2, c, pre_slack_h1, pre_slack_h2):
	"""
	更新拉格朗日乘子 lambda_, mju
	:param lambda_: J (facility)
	:param mju: J (facility)
	:param facility: 设施数量
	:return: lambda_， mju
	"""

	# 本次迭代生成的新的次梯度
	slack_h1 = np.zeros(facility)
	slack_h2 = np.zeros(facility)

	# 生成总的次梯度
	total_slack_h1 = np.zeros(facility)
	total_slack_h2 = np.zeros(facility)

	for j in J:
		slack_h1[j] = sum(primary_z[i, j, k] * h1[i] for i in I for k in K) - c[j] * primary_x[j]
		slack_h2[j] = sum(primary_z[i, j, k] * h2[i] for i in I for k in K) - c[j] * primary_x[j]

	for j in J:
		total_slack_h1[j] = slack_h1[j] + 0.3 * pre_slack_h1[j]
		total_slack_h2[j] = slack_h2[j] + 0.3 * pre_slack_h2[j]

	# 记录分母
	norm = 0
	for j in J:
		norm += np.power(total_slack_h1[j], 2) + np.power(total_slack_h2[j], 2)

	step = scale * (best_value_ubound - best_value) / norm

	# 更新乘子
	for j in J:
		# lambda_[j] = max(lambda_[j] + step * slack_h1[j], 0)
		# mju[j] = max(mju[j] + step * slack_h2[j], 0)

		if lambda_[j] + step * total_slack_h1[j] > 0.001:
			lambda_[j] += step * total_slack_h1[j]
		else:
			lambda_[j] = 0

		if mju[j] + step * total_slack_h2[j] > 0.001:
			mju[j] += step * total_slack_h2[j]
		else:
			mju[j] = 0

	return lambda_, mju, slack_h1, slack_h2
