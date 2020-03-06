#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date: 2014-11-19 21:23:14
# @Last Modified by: Adrien Chardon
# @Last Modified time: 2014-11-23 17:23:24

"""
== Algo ==
Soit N le nombre de points.
Si N < 3
    trivial, jamais de pb
    -> rayon = 0
Sinon N >= 3
    On constitue toutes les combinaisons de 3 points (google k parmi n)
    Pour chaque combinaison
        On verifie qu'il n'y a pas de point a l'interieur (empirique, me demandez pas pourquoi il faut verifier ca !)
        On calcule les coordonnees du cercle circonscrit
        rayon = distance(un point du triangle, centre du cercle circonscrit)
    On se retrouve avec potentiellement plusieurs rayon
    -> on prend le maximum
"""

from math import log, pow, sqrt, pi, atan2


################################################################################
# Comb
################################################################################

# return the *n*th bit of number *byte*
def get_bit(byte, n):
    return (byte & (1 << n)) >> n


# return the length of the binairy number needed to store the number *n*
def get_sizeof_bin(n):
    return int(log(n, 2)) + 1


# return True if the number *n* has *wanted* bit set to 1
def wanted_in_number(n, wanted):
    count = 0
    for i in range(get_sizeof_bin(n)):
        count += get_bit(n, i)
    return count == wanted


# return the list of combinaisons (binairy list, ex : [0, 0, 1, 1, 0, 0, 1])
def get_comb_bin(n, k):
    combs = []
    for comb in range(1, int(pow(2, n))):
        if wanted_in_number(comb, k):
            s = []
            for bit in range(n):
                s.append(get_bit(comb, bit))
            combs.append(s[::-1])
    return combs


################################################################################
# Calc rayon
################################################################################

# Return the coord of the wanted points (which ones has their bool value set to 1 (*comb* list))
def get_coord_from_comb(coords, comb):
    ret = []
    for i in range(len(comb)):
        if comb[i]:
            ret.append(coords[i])
    return ret


# bitch, please
def dist(x, y):
    return sqrt(x * x + y * y)


# compute all the stuff about the mediatrix of a segment
def get_mediatrice_info(a, b):
    m1x = (a[0] + b[0]) / 2.0
    m1y = (a[1] + b[1]) / 2.0
    m1dx = b[0] - a[0]
    m1dy = b[1] - a[1]

    try:
        m1c = -1.0 * m1dx / m1dy
        m1ok = True
    except ZeroDivisionError:
        m1c = 0
        m1ok = False

    return m1x, m1y, m1dx, m1dy, m1c, m1ok


# return the coord of the intersection of two lines
def get_centre_coord(m1x, m1y, m1c, m2x, m2y, m2c):
    y1 = m1y - m1c * m1x
    y2 = m2y - m2c * m2x

    ox1 = 1.0 * (y2 - y1) / (m1c - m2c)
    oy1 = y1 + m1c * ox1

    return ox1, oy1


# check that the angles in the triangle dont exceed pi/2 (90°)
def ft_check_angle(a, b, c):
    tmp1_x = b[0] - a[0]
    tmp1_y = b[1] - a[1]
    a1 = atan2(tmp1_y, tmp1_x)

    tmp2_x = c[0] - a[0]
    tmp2_y = c[1] - a[1]
    a2 = atan2(tmp2_y, tmp2_x)

    af = abs(a1 - a2)
    if af > pi:
        af = pi - af
    return af >= pi / 2.0


# http://openclassrooms.com/forum/sujet/math-point-appartenant-a-un-triangle-18754
# http://blogs.codes-sources.com/kookiz/archive/2009/01/30/c-d-terminer-si-un-point-est-l-int-rieur-d-un-triangle.aspx

def compute_z_coordinate(p1, p2, p3):
    # x1 (y2 - y3) + x2 (y3 - y1) + x3 (y1 - y2)
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]);


def is_point_inside_triangle(triangle, point):
    z1 = compute_z_coordinate(triangle[0], triangle[1], point);
    z2 = compute_z_coordinate(triangle[1], triangle[2], point);
    z3 = compute_z_coordinate(triangle[2], triangle[0], point);

    return (z1 > 0 and z2 > 0 and z3 > 0) or (z1 < 0 and z2 < 0 and z3 < 0)


################################################################################
# Main func
################################################################################

def wifi(n, coords):
    radius = []

    # get the list of all combinaisons (binairy list, ex : [0, 0, 1, 1, 0, 0, 1])
    k = 3
    combs = get_comb_bin(n, k)

    for i in combs:
        pos = get_coord_from_comb(coords, i)

        # check that the triangle has no nested point (dont ask why it's empirical)
        for p in coords:
            if is_point_inside_triangle(pos, p):
                return 0

        r = get_radius_from_triangle(pos)
        radius.append(r)

    # return max of all radius
    if not radius:
        return 0
    else:
        return max(radius)


def get_radius_from_triangle(pos):
    A, B, C = pos

    # if (angle >= pi/2): => return 0 (similaire a un triangle plat, jamais de pb)
    if ft_check_angle(A, B, C) or ft_check_angle(B, C, A) or ft_check_angle(C, A, B):
        return 0

    # MEDIATRICES
    ab_x, ab_y, ab_dx, ab_dy, ab_c, ab_ok = get_mediatrice_info(A, B)
    ac_x, ac_y, ac_dx, ac_dy, ac_c, ac_ok = get_mediatrice_info(A, C)
    bc_x, bc_y, bc_dx, bc_dy, bc_c, bc_ok = get_mediatrice_info(B, C)

    # CENTRE
    ox1, oy1 = 0, 0
    ox2, oy2 = 0, 0
    ox3, oy3 = 0, 0

    if ab_ok and ac_ok:
        ox1, oy1 = get_centre_coord(ab_x, ab_y, ab_c, ac_x, ac_y, ac_c)
    if ab_ok and bc_ok:
        ox2, oy2 = get_centre_coord(ab_x, ab_y, ab_c, bc_x, bc_y, bc_c)
    if ac_ok and bc_ok:
        ox3, oy3 = get_centre_coord(ac_x, ac_y, ac_c, bc_x, bc_y, bc_c)

    b1 = ab_ok * ac_ok
    b2 = ab_ok * bc_ok
    b3 = ac_ok * bc_ok

    c_x = 1.0 * (b1 * ox1 + b2 * ox2 + b3 * ox3) / (b1 + b2 + b3)
    c_y = 1.0 * (b1 * oy1 + b2 * oy2 + b3 * oy3) / (b1 + b2 + b3)

    # RAYON
    r1 = dist(A[0] - c_x, A[1] - c_y)
    r2 = dist(B[0] - c_x, B[1] - c_y)
    r3 = dist(C[0] - c_x, C[1] - c_y)

    r = (r1 + r2 + r3) / 3.0

    # RET
    return r


if __name__ == '__main__':
    N = int(input())
    coords = [tuple([int(e) for e in input().split()]) for _ in range(N)]

    r = wifi(N, coords)

    if int(r) == 0:
        print('0')
    else:
        print('%.3f' % r)
