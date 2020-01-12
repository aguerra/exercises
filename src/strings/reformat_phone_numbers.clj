(ns strings.reformat-phone-numbers
  (:require [clojure.string :as string]
            [clojure.test :refer :all]))

(defn reformat-phone-number
  "You are given a string representing a phone number: at least two
  digits, spaces and/or dashes. Write a function to reformat the phone
  number in such a way that the digits are grouped in blocks separated
  by single dashes."
  [phone-number n]
  (->> (filter #(Character/isDigit %) phone-number)
       (partition-all n)
       (map #(apply str %))
       (string/join "-")))

(deftest tests
  (is (= "004-448-555-583-61" (reformat-phone-number "00-44  48 5555 8361" 3)))
  (is (= "022-198-532-4" (reformat-phone-number "0  -  22 1985--324" 3)))
  (is (= "12-34-56-78-9" (reformat-phone-number "123456789" 2)))
  (is (= "42" (reformat-phone-number "42" 3))))

(run-tests)
