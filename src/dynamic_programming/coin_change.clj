(ns dynamic-programming.coin-change)

(defn min-coins-tests
  "Recurrence relation: f(i, a) = min(f(i, a - d[i]) + 1, f(i - 1, a))."
  [test-fn]
  (assert (= 5 (test-fn 9 [1 2])))
  (assert (= 3 (test-fn 10 [1 3 4])))
  (assert (= 1 (test-fn 5 [1 5])))
  (assert (= 4 (test-fn 16 [1 5 12 19]))))

(def memoized-min-coins
  (memoize (fn [amount denom]
             (cond
               (zero? amount) 0
               (or (< amount 0) (zero? (count denom))) ##Inf
               :else (min (memoized-min-coins amount (butlast denom))
                          (+ 1 (memoized-min-coins (- amount (last denom)) denom)))))))

(run! min-coins-tests [memoized-min-coins])
