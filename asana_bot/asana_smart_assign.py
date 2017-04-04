def smartAssigning(names, statuses, projects, tasks):
    """Analyze team member statuses, projects, and tasks to
    determine which team member is most available for new task 
    assignments."""


    # first remove team members who are on vacation
    for i in range(len(names)):
        print range(len(names))
        print statuses[i]
        if statuses[i] == True:
            names.pop(i)
            statuses.pop(i)
            projects.pop(i)
            tasks.pop(i)

    # then, compare team member projects and tasks to find min

    for i in range(len(names)):
        if projects[i] != min(projects):
            names.pop(i)
            statuses.pop(i)
            projects.pop(i)
            tasks.pop(i)

    if len(names) == 1:
        return names[0]

    for i in range(len(names)):
        if tasks[i] != min(tasks):
            names.pop(i)
            statuses.pop(i)
            projects.pop(i)
            tasks.pop(i)

    #return names[0]


    # first, organize team members in a dict for quick lookup
    # team_member_availability = {}
    
    # binary_statuses = [] # converting to 1 or 0 to compare later
    
    # for s in statuses:
    #     if s == True:
    #         binary_statuses.append(1)
    #     elif s == False:
    #         binary_statuses.append(0)
    
    # for i in range(len(names)):
    #     if names[i] not in team_member_availability:
    #         team_member_availability[names[i]] = (binary_statuses[i], projects[i], tasks[i])
    
    # team_member_availability looks like:
    # { 'John': (false, 2, 16), 
    #   'Martin': (false, 1, 5) }
    
    # next, determine which team member is more available:
    






names = ['John', 'Martin', 'Luke']
statuses = [False, True, False]
projects = [1, 0, 2]
tasks = [2, 0, 1]

smartAssigning(names, statuses, projects, tasks)