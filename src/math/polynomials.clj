(ns math.polynomials
  (:require [clojure.test :refer :all]))

(defn add
  "Choose a representation and write a function to add polynomials.
  A polynomial is represented by a map where the keys are the
  powers and the values are coefficients."
  ([p q]
   (merge-with + p q))
  ([p q & more]
   (reduce add (add p q) more)))

(deftest tests
  (is (= {0 2 1 2} (add {0 1 1 1} {0 1 1 1})))
  (is (= {0 0 1 0} (add {0 1 1 1} {0 -1 1 -1})))
  (is (= {1 5 4 11 5 12 6 3} (add {1 2 4 16 5 22} {1 3 4 -5 5 -10 6 3})))
  (is (= {0 1 1 6 4 11 5 12 6 3} (add {1 2 4 16 5 22} {1 3 4 -5 5 -10 6 3} {0 1 1 1}))))

(run-tests)
