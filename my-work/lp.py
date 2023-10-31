from ortools.linear_solver import pywraplp

def LinearProgrammingProblemA():

    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    p1 = solver.NumVar(0, 1, "p1")
    p2 = solver.NumVar(0, 1, "p2")
    p3 = solver.NumVar(0, 1, "p3")
    p4 = solver.NumVar(0, 1, "p4")
    P = solver.NumVar(-solver.Infinity(), solver.Infinity(), "P")

    print("Number of variables =", solver.NumVariables())

    solver.Add(-3 * p1 - (3/2) * p2 - p3 - p4 + P >= 0)

    solver.Add(-p1 - 2 * p2 - (4/3) * p3 - (4/3) * p4 + P >= 0)

    solver.Add(-p1 - p2 - (5/3) * p3 - (5/3) * p4 + P >= 0)

    solver.Add(-p1 - p2 - p3 - 2 * p4 + P >= 0)

    solver.Add(p1 + p2 + p3 + p4 == 1)

    print("Number of constraints =", solver.NumConstraints())

    # Objective function: 3x + 4y.
    solver.Minimize(P)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        print("p1 =", p1.solution_value())
        print("p2 =", p2.solution_value())
        print("p3 =", p3.solution_value())
        print("p4 =", p4.solution_value())
    else:
        print("The problem does not have an optimal solution.")

    print("\nAdvanced usage:")
    print("Problem solved in %f milliseconds" % solver.wall_time())
    print("Problem solved in %d iterations" % solver.iterations())

def LinearProgrammingProblemB():

    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    q1 = solver.NumVar(0, 1, "q1")
    q2 = solver.NumVar(0, 1, "q2")
    q3 = solver.NumVar(0, 1, "q3")
    q4 = solver.NumVar(0, 1, "q4")
    Q = solver.NumVar(-solver.Infinity(), solver.Infinity(), "Q")

    print("Number of variables =", solver.NumVariables())

    solver.Add(-(3 * q1 + q2 + q3 + q4) + Q <= 0)

    # Constraint 1: 3x - y >= 0.
    solver.Add(-(3/2 * q1 + 2 * q2 + q3 + q4) + Q <= 0)

    # Constraint 2: x - y <= 2.
    solver.Add(-(q1 + (4/3) * q2 + (5/3) * q3 + q4) + Q <= 0)

    solver.Add(-(q1 + (4/3) * q2 + (5/3) * q3 + 2 * q4) + Q <= 0)

    solver.Add(q1 + q2 + q3 + q4 == 1)

    print("Number of constraints =", solver.NumConstraints())

    # Objective function: 3x + 4y.
    solver.Maximize(Q)

    # Solve the system.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        print("q1 =", q1.solution_value())
        print("q2 =", q2.solution_value())
        print("q3 =", q3.solution_value())
        print("q4 =", q4.solution_value())
    else:
        print("The problem does not have an optimal solution.")

    print("\nAdvanced usage:")
    print("Problem solved in %f milliseconds" % solver.wall_time())
    print("Problem solved in %d iterations" % solver.iterations())

LinearProgrammingProblemA()
LinearProgrammingProblemB()







