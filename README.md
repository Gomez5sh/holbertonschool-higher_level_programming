.\"Modified from man(1) of FreeBSD, the NetBSD mdoc.template, and mdoc.samples.
.\"See Also:
.\"man mdoc.samples for a complete listing of options
.\"man mdoc for the short list of editing options
.\"/usr/share/misc/mdoc.template
.Dd 11/26/19               \" DATE
.Dt Simple_shell 1      \" Program name and manual section number
.Os Darwin
.Sh SIMPLE SHELL                 \" Section Header - required - don't modify
.Nm Simple Shell
.\" The following lines are read in generating the apropos(man -k) database. Use only key
.\" words here as the database is built based on the words here and in the .ND line.
.\" Use .Nm macro to designate other names for the documented program.
.Nd The simple Shell proyect.
.Sh SYNOPSIS             \" Section Header - required - don't modify
.Nm
.Op options              \" [-abcd]
.Op Command_string | file         \" [-a path]
.Sh DESCRIPTION          \" Section Header - required - don't modify
Use the .Nm macro to refer to your program throughout the man page like such:
.Nm
Underlining is accomplished with the .Ar macro like this:
.Ar underlined text .
.Pp                      \" Inserts a space
A list of items with descriptions:
.Bl -tag -width -indent  \" Begins a tagged list
.It item a               \" Each item preceded by .It macro
Description of item a
.It item b
Description of item b
.El                      \" Ends the list
.Pp
A list of flags and their descriptions:
.Bl -tag -width -indent  \" Differs from above in tag removed
.It Fl a                 \"-a flag as a list item
Description of -a flag
.It Fl b
Description of -b flag
.El                      \" Ends the list
.Pp
.\" .Sh ENVIRONMENT      \" May not be needed
.\" .Bl -tag -width "ENV_VAR_1" -indent \" ENV_VAR_1 is width of the string ENV_VAR_1
.\" .It Ev ENV_VAR_1
.\" Description of ENV_VAR_1
.\" .It Ev ENV_VAR_2
.\" Description of ENV_VAR_2
.\" .El
.Sh FILES                \" File used or created by the topic of the man page
.Bl -tag -width "/Users/joeuser/Library/really_long_file_name" -compact
.It Pa /usr/share/file_name
FILE_1 description
.It Pa /Users/joeuser/Library/really_long_file_name
FILE_2 description
.El                      \" Ends the list
.\" .Sh DIAGNOSTICS       \" May not be needed
.\" .Bl -diag
.\" .It Diagnostic Tag
.\" Diagnostic informtion here.
.\" .It Diagnostic Tag
.\" Diagnostic informtion here.
.\" .El
.Sh SEE ALSO
.\" List links in ascending order by section, alphabetically within a section.
.\" Please do not reference files that do not exist without filing a bug report
.Xr a 1 ,
.Xr b 1 ,
.Xr c 1 ,
.Xr a 2 ,
.Xr b 2 ,
.Xr a 3 ,
.Xr b 3
.\" .Sh BUGS              \" Document known, unremedied bugs
# holbertonschool-higher_level_programming
# holbertonschool-higher_level_programming
