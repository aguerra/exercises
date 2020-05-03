(ns sorting.quicksort
  (:require [clojure.test :refer :all]))

(defn naive-quicksort
  [[pivot & rst :as coll]]
  (if pivot
    (let [less? #(< % pivot)]
      (lazy-cat (naive-quicksort (filter less? rst))
                [pivot]
                (naive-quicksort (remove less? rst))))
    coll))

(deftest tests
  (are [coll sorted] (= sorted (naive-quicksort coll))
    []              '()
    [1 2 3 4 5]     '(1 2 3 4 5)
    [5 4 3 2 1]     '(1 2 3 4 5)
    '(7 8 1 10 2)   [1 2 7 8 10]
    #{9 10 2 46 20} [2 9 10 20 46]))

(run-tests)
