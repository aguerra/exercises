(ns recursion.powerset
  (:require [clojure.test :refer :all]))

(defn powerset
  "Write a function that, given a set, generates its power set."
  [coll]
  (loop [[x & r] (seq coll)
         p [[]]]
    (if x
      (recur r (concat p (map (partial cons x) p)))
      p)))

(defn powerset-reduce
  [coll]
  (reduce (fn [r x] (concat r (map (partial cons x) r))) [[]] (seq coll)))

(deftest tests
  (are [r coll] (= r (powerset coll) (powerset-reduce coll))
    [[]]                                       []
    [[] [1]]                                   '(1)
    '(() (1) (2) (2 1))                        #{1 2}
    [[] [[:a 1]]]                              {:a 1}
    [[] [1] [2] [2 1] [3] [3 1] [3 2] [3 2 1]] [1 2 3]))

(run-tests)
