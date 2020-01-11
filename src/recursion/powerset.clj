(ns recursion.powerset
  (:require [clojure.test :refer :all]))

(defn powerset
  "Write a function that, given a set, generates its power set."
  [s]
  (loop [[x & r] s
         p '(())]
    (if x
      (recur r (concat p (map (partial cons x) p)))
      p)))

(deftest powerset-tests
  (is (= [[]] (powerset [])))
  (is (= [[] [1]] (powerset '(1))))
  (is (= [[] [1] [2] [2 1]] (powerset #{1 2})))
  (is (= [[] [1] [2] [2 1] [3] [3 1] [3 2] [3 2 1]] (powerset [1 2 3]))))

(run-tests)
