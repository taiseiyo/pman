(defun pman ()
  "pman is python module manual"
  (interactive)
  (setq name (read-string "enter -m module or -f function : "))
  (setq command (concat "env python3 ~/bin/pman.py " name))
  (prepare_window)
  (compile command)
  )

(defun prepare_window ()
  (setq split_flag (one-window-p))
  (if (eq t split_flag)
      (progn 
	(split-window-horizontally))
  )
  )

(provide 'pman)

