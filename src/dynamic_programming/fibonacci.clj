(ns dynamic-programming.fibonacci)

(def memoize-fib
  (memoize (fn [n]
             (if (< n 2) n
                 (+ (memoize-fib (dec n)) (memoize-fib (- n 2)))))))

(defn bottom-up-fib [n]
  (-> (map first (iterate (fn [[a b]] [b (+' a b)]) [0 1]))
      (nth n)))
