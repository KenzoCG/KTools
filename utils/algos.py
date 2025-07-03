
# ------------------------------------------------------------------------------- #
# LIST
# ------------------------------------------------------------------------------- #

def items_to_pairwise_closed_loop(items=[]):
    looped = []
    for i in range(len(items)):
        looped.extend([items[i], items[(i + 1) % len(items)]])
    return looped
