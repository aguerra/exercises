(ns sorting.quicksort
  (:require [clojure.test :refer :all]))

(defn quicksort
  [[pivot & rst :as coll]]
  (if pivot
    (let [less? #(< % pivot)]
      (lazy-cat (quicksort (filter less? rst))
                [pivot]
                (quicksort (remove less? rst))))
    coll))

(deftest tests
  (are [coll sorted] (= sorted (quicksort coll))
    []              '()
    [1 2 3 4 5]     '(1 2 3 4 5)
    [5 4 3 2 1]     '(1 2 3 4 5)
    '(7 8 1 10 2)   [1 2 7 8 10]
    #{9 10 2 46 20} [2 9 10 20 46]))

(run-tests)
