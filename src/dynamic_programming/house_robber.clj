(ns dynamic-programming.house-robber
  (:require [clojure.test :refer :all]))

(def memoized-house-robber
  "You are a robber who has found a block of houses to rob. Each house
  has a non-negative v worth of value inside that you can
  steal. However, due to the way the security systems of the houses
  are connected, you’ll get caught if you rob two adjacent
  houses. What’s the maximum value you can steal from the block? Solution:

  * Steal from house i, but then you have to maximize the stolen value
  up to house i−2 and add vi to your running total.

  * Don’t steal from house i, in which case you’re free to maximize
  the stolen value up to house i−1 and add nothing to your running
  total.

  Recurrence relation: f(i) =  max(v[i] + f(i-2), f(i-1))."
  (memoize (fn [values]
             (let [but-last (butlast values)]
               (if (< (count values) 1) 0
                   (max (memoized-house-robber but-last)
                        (+ (last values) (memoized-house-robber (butlast but-last)))))))))

(defn bottom-up-house-robber
  [values]
  (loop [v values
         a 0
         b 0]
    (if (zero? (count v)) b
        (recur (butlast v) b (max b (+ a (last v)))))))

(deftest tests
  (are [v r] (= r (memoized-house-robber v) (bottom-up-house-robber v))
    []            0
    [1]           1
    [3 1]         3
    [3 10 3 1 2] 12) )

(run-tests)
