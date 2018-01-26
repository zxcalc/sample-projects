from quanto.util.Scripting import *

simps0 = load_rules([
  "axioms/red_copy", "axioms/green_copy",
  "axioms/red_sp", "axioms/green_sp",
  "axioms/hopf",
  "axioms/red_scalar", "axioms/green_scalar",
  "axioms/red_loop", "axioms/green_loop"])

simps = simps0 + load_rules(["axioms/green_id", "axioms/red_id"])

green_id_inv = load_rule("axioms/green_id").inverse()
red_id_inv = load_rule("axioms/red_id").inverse()
rotate = load_rule("theorems/rotate_targeted")


def num_boundary_X(g):
  return len([v for v in verts(g)
    if g.isBoundary(v) and g.isAdjacentToType(v, 'X')])

def next_rotation_Z(g):
  vs = [(g.arity(v),v) for v in verts(g)
    if g.typeOf(v) == 'Z' and
       vertex_angle_is(g, v, '0') and
       not g.isAdjacentToBoundary(v)]
  if (len(vs) == 0): return None
  else: return min(vs)[1]


simproc = (
  REDUCE(simps) >>
  REDUCE_METRIC(green_id_inv, num_boundary_X) >>
  REPEAT(
    REDUCE_TARGETED(rotate, "v10", next_rotation_Z) >>
    REDUCE(simps0)
  ) >>
  REDUCE(simps)
)


register_simproc("rotate-simp", simproc)


