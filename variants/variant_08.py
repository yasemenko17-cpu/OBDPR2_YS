def decompose_bcnf(attrs, fds):
    """
    Розкладає схему на відношення у BCNF.
    attrs: frozenset атрибутів
    fds: список пар (lhs, rhs) із frozenset
    Повертає список frozenset відношень.
    """
    relations = [frozenset(attrs)]
    result = []
    
    while relations:
        R = relations.pop(0)
        
        violating_fd = None
        for lhs, rhs in fds:
            if lhs.issubset(R):
                # Локальна функція замикання для побудови X+
                cl = set(lhs)
                changed = True
                while changed:
                    changed = False
                    for flhs, frhs in fds:
                        if flhs.issubset(cl) and not frhs.issubset(cl):
                            cl.update(frhs)
                            changed = True
                            
                cl_R = frozenset(cl.intersection(R))
                
                # Перевірка порушення BCNF: lhs не є надключем для R
                if not R.issubset(cl_R) and len(cl_R) > len(lhs):
                    violating_fd = (lhs, cl_R)
                    break
        
        if violating_fd:
            lhs, cl_R = violating_fd
            R1 = cl_R
            R2 = frozenset((R - cl_R).union(lhs))
            relations.append(R1)
            relations.append(R2)
        else:
            if R not in result:
                result.append(R)
                
    return result