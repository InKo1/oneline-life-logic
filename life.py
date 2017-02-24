from itertools import product, chain
from functools import reduce
from collections import Counter


def _get_neighbours_coords(point):
    """Соседние координаты точки point"""
    return map(
        lambda d: (point[0] + d[0], point[1] + d[1]),
        product((1, 0, -1), (1, 0, -1))
    )


def _get_dead_neighbours_coords(point, field):
    """Соседние координаты точки point, в которых нет жизни"""
    return filter(
        lambda p: not (p in field),
        _get_neighbours_coords(point)
    )


def _get_neigbours_size(point, field):
    """Количество соседних координат точки point, в которых есть жизнь"""
    return reduce(
        lambda a, b: a + b,
        map(lambda p: p in field, _get_neighbours_coords(point))
    ) - 1


def _get_dead_cells_with_alive_neighbours_coords(field):
    """Координаты, в которых нет жизни, но у которых есть живые соседи"""
    return chain.from_iterable(
        map(
            lambda p: _get_dead_neighbours_coords(p, field),
            field
        )
    )


def _get_cells_who_must_live(field):
    """Координаты точек, которые должны остаться живыми на следующей итерации"""
    return filter(
        lambda p: 2 <= _get_neigbours_size(p, field) <= 3,
        field
    )


def _get_cells_who_must_born(field):
    """Координаты точек, в которых должна появиться жизнь на следующей итерации"""
    return map(
        lambda p: p[0],
        filter(
            lambda p: p[1] == 3,
            Counter(
                _get_dead_cells_with_alive_neighbours_coords(field)
            ).items()
        )
    )


def get_next_generation(field):
    """Следующая итерация"""
    return set(
        chain(
            _get_cells_who_must_live(field),
            _get_cells_who_must_born(field)
        )
    )
