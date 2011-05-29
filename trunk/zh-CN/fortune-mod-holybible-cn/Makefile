# Copyright 1999-2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

FORTUNE_DIR = /usr/share/fortune
NAME=holybible-cn

$(NAME).dat: $(NAME)
	strfile $(NAME)

.PHONY: install uninstall

install: $(NAME).dat
	install -m 0644 $(NAME) $(NAME).dat $(FORTUNE_DIR)
	install -m 0755 gfortune-$(NAME) /usr/bin

uninstall:
	rm $(FORTUNE_DIR)/$(NAME) $(FORTUNE_DIR)/$(NAME).dat $(FORTUNE_DIR)/$(NAME).u8 /usr/bin/gfortune-$(NAME)
