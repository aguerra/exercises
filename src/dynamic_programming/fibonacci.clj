(ns dynamic-programming.fibonacci
  (:require [clojure.test :refer :all]))

(def memoized-fib
  "Recurrence relation: f(i) = f(i-1) + f(i-2)."
  (memoize (fn [n]
             (if (< n 2) n
                 (+ (memoized-fib (dec n)) (memoized-fib (- n 2)))))))

(defn bottom-up-fib
  [n]
  (-> (map first (iterate (fn [[a b]] [b (+' a b)]) [0 1]))
      (nth n)))

(deftest tests
  (are [n r] (= r (memoized-fib n) (bottom-up-fib n))
    0     0
    1     1
    2     1
    5     5
    7    13
    9    34
   20  6765))

(run-tests)
