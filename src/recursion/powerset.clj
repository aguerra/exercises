(ns recursion.powerset
  (:require [clojure.set :refer [union]]
            [clojure.test :refer :all]))

(defn powerset
  "Write a function that, given a set, generates its power set."
  [s]
  (loop [[x & r] s
         p #{#{}}]
    (if x
      (recur r (union p (map #(conj % x) p)))
      p)))

(deftest powerset-tests
  (is (= #{#{}} (powerset #{})))
  (is (= #{#{} #{1}} (powerset #{1})))
  (is (= #{#{} #{1} #{2} #{1 2}} (powerset #{1 2})))
  (is (= #{#{} #{1} #{2} #{3} #{1 2} #{2 3} #{1 3} #{1 2 3}} (powerset #{1 2 3}))))

(run-tests)
