# Aura notes from aura-aima

Bugs are filed upstream; this file keeps the workarounds in one place.

| Issue | What | Workaround here |
|---|---|---|
| [#4487](https://github.com/cybrid-systems/aura/issues/4487) | `'(a . 1)` reads as `(cons a 1 …)`, circular with symbols; `display` hangs | data tables use proper lists `(Zerind 75)`; pairs built with `cons` at runtime (tests too) |
| [#4488](https://github.com/cybrid-systems/aura/issues/4488) | `eqv?` `exact->inexact` `inexact` `exact` `truncate` `ceiling` `assv` `memv` … documented as core but unbound in Soft | `(* 1.0 n)` for float conversion; local `sym-assq` |
| [#4489](https://github.com/cybrid-systems/aura/issues/4489) | hash keys: floats / lists / vectors compared by identity | every searcher takes a `key` function mapping a state to an int (8-puzzle base 9, grid `x*100000+y`) or symbol |
| [#4490](https://github.com/cybrid-systems/aura/issues/4490) | quoted `#t`/`#f` read as `1`/`0`; quoted `#(...)` is not a vector; `0` is falsy | expected values with booleans built with `(list ...)`; vectors with `(vector ...)` |
| [#4491](https://github.com/cybrid-systems/aura/issues/4491) | integer `0` is falsy in `if`/`cond`/`and`/`or` (`0.0` is truthy) | **fixed** upstream (only `#f` is false): workaround removed, `index-of` returns index-or-`#f` again |
| [#4492](https://github.com/cybrid-systems/aura/issues/4492) | builtin `map` results got corrupted once f allocated (nested map) | FIXED upstream; `lmap` removed, builtin `map` used everywhere (385 checks green) |

Smaller notes (not filed):

- Games use a ±1e9 sentinel for -inf/+inf (utilities are small ints), so no float infinities are needed.
- No `define-record-type`; nodes and problems are plain vectors with accessors.
- No `assq` / `assoc` / `memq` / `string->symbol` / `vector-map` / `vector-copy` (listed in #4488).
- `current-milliseconds` is not bound; `current-time-ms` is.
- Throughput under heavy machine load (load avg 40–60 during this work) is low: the
  Romania suite (73 checks, includes 2.9k-state BFS tree search) takes about 2 min.
