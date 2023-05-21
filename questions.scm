(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists

;; Define new procedure 'enumerate' takes parameter s 
;; representing the input list
(define (enumerate s)
  ; BEGIN PROBLEM 15

  ;; create a recursive helper procedure takes 3 parameters
  ;; list s, index starts with 0, empty result
  (let loop ((lst s) (index 0) (result '()))
    ;; If reached empty list, reverse the result
    (cond ((null? lst) (reverse result))
      ;; Otherwise, keep calling the loop procedure, use cdr to get the last element in the pair
      ;; add 1 to the index, and construct a list with two-elements, 
      ;; Index and Value, EX (0 5), where 0 is index and 5 is value
      ;; Finally, return the result
      (else (loop (cdr lst) (+ index 1) (cons (list index (car lst)) result ))))))

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2) (if (or (null? list1) (null? list2))
                                  (if (null? list1)
                                      (if (null? list2)
                                      '()
                                      list2)
                                      list1)
                                  (if (ordered? (car list1) (car list2))
                                      (cons (car list1) (merge ordered? (cdr list1) list2))
                                      (cons (car list2) (merge ordered? list1 (cdr list2))))))

;; Optional Problem

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM
           'replace-this-line
           ; END OPTIONAL PROBLEM
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM
           'replace-this-line
           ; END OPTIONAL PROBLEM
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM
         'replace-this-line
         ; END OPTIONAL PROBLEM
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  'replace-this-line)
