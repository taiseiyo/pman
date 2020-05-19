(defun pman ()
  "pman is python module manual"
  (interactive)
  (setq name (read-string "enter -m module or -f function : "))
  (setq command (concat "env python3 ~/bin/pman.py " name))
  (compile command))
				    
(provide 'pman)
