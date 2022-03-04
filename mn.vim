" Vim syntax file 
" Language:	Music Note file 
" Last Change:	2022 Mar 03 
" Author :	iClaud

" Quit when a (custom) syntax file was already loaded
if exists("b:current_syntax")
  finish
endif

let s:cpo_save = &cpo
set cpo&vim

syn match regular "^.*$"
syn match songName "^=.*=$"
syn match musicNotionLine "^[0-7\[\]()# ]*$" contains=highNote contains=lowNote contains=normal
syn match musicNotionLine "^[0-7\[\]()# ]*$" 
syn match highNote "\[[0-7]\]"
syn match highNote "\[#[0-7]\]"
syn match lowNote "(#[0-7])"
syn match lowNote "([0-7])"
syn match normal "[0-7]"


hi def link regular Ignore 
hi def link songName Statement
hi def link musicNotionLine Comment
hi def link highNote Float 
hi def link lowNote Keyword
hi def link normal Tag

let b:current_syntax = "mn"

let &cpo = s:cpo_save
unlet s:cpo_save
" vim: ts=8 sw=2
