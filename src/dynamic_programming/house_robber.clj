(ns dynamic-programming.house-robber)

; Recurrence relation: f(i) =  max(values[i] + f(i-2), f(i-1))

(defn tests
  [test-fn]
  (assert (= 0 (test-fn [])))
  (assert (= 1 (test-fn [1])))
  (assert (= 3 (test-fn [3 1])))
  (assert (= 12 (test-fn [3 10 3 1 2]))))

(def memoize-hr
  (memoize (fn [values]
             (let [n (count values)
                   but-last (butlast values)]
               (if (< n 1) 0
                   (max (memoize-hr but-last)
                        (+ (last values) (memoize-hr (butlast but-last)))))))))

(defn bottom-up-hr
  [values]
  (loop [n (-> values count dec)
         a 0
         b 0]
    (if (< n 0) b
        (recur (dec n) b (max b (+ a (nth values n)))))))

; TODO: lazy seq version

(run! tests [memoize-hr bottom-up-hr])
