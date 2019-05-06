from pm4pyws.session_manager.versions.basic_log_manager import BasicLogSessionHandler

BASIC_LOG_SESSION_HANDLING = "basic_log_session_handling"

VERSIONS = {BASIC_LOG_SESSION_HANDLING: BasicLogSessionHandler}


def apply(ex, variant=BASIC_LOG_SESSION_HANDLING):
    """
    Gets the session handler according to the variant

    Parameters
    -----------
    ex
        Exception handler
    variant
        Variant

    Returns
    -----------
    session_handler
        Session handler
    """
    return VERSIONS[variant](ex)
