def is_consistent(region, color, assignment, constraints):
    for neighbor in constraints[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def backtrack(regions, domains, constraints, assignment={}):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)

    for color in domains[region]:
        if is_consistent(region, color, assignment, constraints):
            assignment[region] = color

            result = backtrack(
                regions, domains, constraints, assignment
            )

            if result:
                return result

            del assignment[region]

    return None


regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

domains = {
    r: ['red', 'green', 'blue']
    for r in regions
}

constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

result = backtrack(regions, domains, constraints)

print("Coloring:", result)