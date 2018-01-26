from quanto.util.Scripting import *

simps = load_rules([
  "axioms/red_copy", "axioms/red_sp", "axioms/green_sp", "axioms/hopf",
  "axioms/red_scalar", "axioms/green_scalar", "axioms/green_id",
  "axioms/red_id", "axioms/red_loop", "axioms/green_loop"])

register_simproc("basic-simp", REDUCE(simps))


