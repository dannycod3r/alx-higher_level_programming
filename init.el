;; basic config

;; set theme
(load-theme 'tango-dark)

(set-fringe-mode 10) ;; give space

;; autoclose brackets
(require 'cc-mode)
(add-hook 'c-mode-common-hook 'electric-pair-mode)

;; line number in all buffers
(global-display-line-numbers-mode 1)

;; tabs, etc
(setq c-default-style "bsd"
      c-basic-offset 8
      tab-width 8
      indent-tabs-mode t)

(require 'whitespace)
(setq whitespace-style '(face empty lines-tail trailing))
(global-whitespace-mode t)

;; column numbers
(setq column-number-mode t)

;; Keyboard-centric user interface
(setq inhibit-startup-message t)
(tool-bar-mode -1)
(menu-bar-mode -1)
(scroll-bar-mode -1)
