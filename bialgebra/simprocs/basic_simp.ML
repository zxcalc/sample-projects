open RG_SimpUtil


val simps = load_ruleset [
  "axioms/red-merge", "axioms/red-id",
  "axioms/green-merge", "axioms/green-id",
  "axioms/distribute"
];

val simproc = REDUCE_ALL simps;

register_simproc ("basic_simp", simproc);




