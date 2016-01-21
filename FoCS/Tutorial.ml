let c_to_f a = a *. 9.0 /. 5.0 +. 32.0

let add (x, y) = x + y

let rec sumto_helper (index, n, result) = 
    if index <= n then 
      sumto_helper(index + 1, n, result + index)
    else result

(* let sumto (n) = sumto_helper(0, n, 0) *)

let rec sumto (n) = if n = 0 then 0 else sumto(n - 1) + n

(* or even better: *)
let add (x,y) = x + y

(* let first p = match p with (x,y) -> x  *) (* useful for type checking first component *)