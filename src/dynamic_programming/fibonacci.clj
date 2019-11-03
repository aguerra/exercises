(ns dynamic-programming.fibonacci)

(defn fibonacci-tests
  "Recurrence relation: f(i) = f(i-1) + f(i-2)."
  [test-fn]
  (assert (= 0 (test-fn 0)))
  (assert (= 1 (test-fn 1)))
  (assert (= 1 (test-fn 2)))
  (assert (= 5 (test-fn 5)))
  (assert (= 13 (test-fn 7)))
  (assert (= 34 (test-fn 9))))

(def memoized-fib
  (memoize (fn [n]
             (if (< n 2) n
                 (+ (memoized-fib (dec n)) (memoized-fib (- n 2)))))))

(defn bottom-up-fib
  [n]
  (-> (map first (iterate (fn [[a b]] [b (+' a b)]) [0 1]))
      (nth n)))

(run! fibonacci-tests [memoized-fib bottom-up-fib])
