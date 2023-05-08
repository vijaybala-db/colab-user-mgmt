# USAGE   ./move.sh {destination_workspace}
# EXAMPLE ./move.sh slalom

# From the source workspace, run the following
DESTINATION_WORKSPACE=$1
terraform state list | xargs -I {} terraform state mv "{}" "module.$DESTINATION_WORKSPACE.{}"
