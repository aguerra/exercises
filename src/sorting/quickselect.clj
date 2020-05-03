(ns sorting.quickselect
  (:require [clojure.test :refer :all]))

(defn naive-quickselect
  "Find the k smallest element"
  [[pivot & rst :as coll] k]
  (when pivot
    (let [less? #(< % pivot)
          left  (filter less? rst)]
      (condp #(%1 k %2) (count left)
        < (naive-quickselect left k)
        > (naive-quickselect (remove less? rst) (dec k))
        pivot))))

(deftest tests
  (are [coll k r] (= r (naive-quickselect coll k))
    []                1   nil
    [1 2 3]           0   1
    [4 3 2 1]         2   3
    '(32 1 56 3 4 10) 2   4
    #{22 100 4 8 12}  3   22))

(run-tests)
