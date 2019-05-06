class LogHandler(object):
    def __init__(self, ex):
        # exception handler
        self.ex = ex

    def get_handlers(self):
        """
        Gets the current set of handlers

        Returns
        -----------
        handlers
            Handlers
        """
        raise Exception("session_handler get_handlers not implemented!")

    def get_handler_for_process_and_session(self, process, session):
        """
        Gets an handler for a given process and session

        Parameters
        -------------
        process
            Process
        session
            Session

        Returns
        -------------
        handler
            Handler
        """
        raise Exception("session_handler get_handler_for_process_and_session not implemented!")


    def set_handler_for_process_and_session(self, process, session, handler):
        """
        Sets the handler for the current process and session

        Parameters
        -------------
        process
            Process
        session
            Session
        handler
            Handler
        """
        raise Exception("session_handler set_handler_for_process_and_session not implemented!")


    def check_is_admin(self, user):
        """
        Checks if the user is an administrator

        Parameters
        -------------
        user
            User

        Returns
        -------------
        boolean
            Boolean value
        """
        raise Exception("session_handler check_is_admin not implemented!")

    def manage_upload(self, user, basename, filepath):
        """
        Manages an event log that is uploaded

        Parameters
        ------------
        user
            Current user
        basename
            Name of the log
        filepath
            Log path
        """
        raise Exception("session_handler manage_upload not implemented!")

    def check_user_log_visibility(self, user, process):
        """
        Checks if the user has visibility on the given process

        Parameters
        -------------
        user
            User
        process
            Process
        """
        raise Exception("session_handler check_user_log_visibility not implemented!")


    def check_user_enabled_upload(self, user):
        """
        Checks if the user is enabled to upload a log

        Parameters
        ------------
        user
            User

        Returns
        ------------
        boolean
            Boolean value
        """
        raise Exception("session_handler check_user_enabled_upload not implemented!")


    def check_user_enabled_download(self, user, process):
        """
        Checks if the user is enabled to download a log

        Parameters
        ------------
        user
            User
        process
            Process

        Returns
        ------------
        boolean
            Boolean value
        """
        raise Exception("session_handler check_user_enabled_download not implemented!")


    def load_log_static(self, log_name, file_path, parameters=None):
        """
        Loads an event log inside the known handlers

        Parameters
        ------------
        log_name
            Log name
        file_path
            Full path (in the services machine) to the log
        parameters
            Possible parameters
        """
        raise Exception("session_handler load_log_static not implemented!")

