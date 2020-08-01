from primary_model_by_docplex.mp.model import Model
from primary_model_by_docplex.util.environment import get_environment


model = Model(name='sum_if')
model.x = [i for i in range(5)]
count_x = model.x
x = model.binary_var_list(count_x, name='x')
model.add_constraints((x[i] <= 10) for i in count_x)
model.minimize(model.sum(x[i] for i in count_x))
if model.solve():
    for i in range(4):
        print(x[i].solution_value)
    print("目标函数为：", model.objective_value)
    # Save the CPLEX solution as "solution.json" program output
    with get_environment().get_output_stream("solution.json") as fp:
        model.solution.export(fp, "json")
else:
    print("Problem has no solution")