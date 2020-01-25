(ns dynamic-programming.coin-change
  (:require [clojure.test :refer :all]))

(def memoized-min-coins
  "Determine the fewest number of coins you can use to make a certain
  amount if you have coins of a certain set of denominations. You can
  use any quantity of each denomination and assume the denominations
  are given in increasing order of value. Solution:

  * Use one coin of the highest denomination, the number of coins used
  goes up by one.

  * Don’t use any coin of the highest denomination, move to next one
  and the number of coins used stays the same.

  Recurrence relation: f(i, a) = min(f(i, a-d[i]) + 1, f(i-1, a))."
  (memoize (fn [amount denom]
             (cond
               (zero? amount) 0
               (or (< amount 0) (zero? (count denom))) ##Inf
               :else (min (memoized-min-coins amount (butlast denom))
                          (+ 1 (memoized-min-coins (- amount (last denom)) denom)))))))

(deftest tests
  (is (= 5 (memoized-min-coins 9 [1 2])))
  (is (= 3 (memoized-min-coins 10 [1 2 4])))
  (is (= 1 (memoized-min-coins 5 [1 5])))
  (is (= 4 (memoized-min-coins 16 [1 5 12 19]))))

(run-tests)
