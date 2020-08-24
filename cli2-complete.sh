_cli2_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _CLI2_COMPLETE=complete $1 ) )
    return 0
}

complete -F _cli2_completion -o default cli2;
