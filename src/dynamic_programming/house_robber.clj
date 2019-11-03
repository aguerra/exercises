(ns dynamic-programming.house-robber)

(defn house-robber-tests
  "Recurrence relation: f(i) =  max(v[i] + f(i-2), f(i-1))."
  [test-fn]
  (assert (= 0 (test-fn [])))
  (assert (= 1 (test-fn [1])))
  (assert (= 3 (test-fn [3 1])))
  (assert (= 12 (test-fn [3 10 3 1 2]))))

(def memoized-house-robber
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

(run! house-robber-tests [memoized-house-robber bottom-up-house-robber])
