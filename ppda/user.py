from base import Base


class User(Base):
    """
    Class to represent a user in SIS system
    """

    ATTRIBUTES = [
        "name",
        "owner",
        "creation",
        "modified",
        "modified_by",
        "docstatus",
        "idx",
        "enabled",
        "email",
        "first_name",
        "middle_name",
        "last_name",
        "full_name",
        "username",
        "language",
        "time_zone",
        "send_welcome_email",
        "unsubscribed",
        "user_image",
        "role_profile_name",
        "roles",
        "module_profile",
        "home_settings",
        "gender",
        "birth_date",
        "interest",
        "phone",
        "location",
        "bio",
        "mobile_no",
        "mute_sounds",
        "desk_theme",
        "banner_image",
        "new_password",
        "logout_all_sessions",
        "reset_password_key",
        "last_reset_password_key_generated_on",
        "last_password_reset_date",
        "redirect_url",
        "document_follow_notify",
        "document_follow_frequency",
        "follow_created_documents",
        "follow_commented_documents",
        "follow_liked_documents",
        "follow_assigned_documents",
        "follow_shared_documents",
        "email_signature",
        "thread_notify",
        "send_me_a_copy",
        "allowed_in_mentions",
        "default_workspace",
        "simultaneous_sessions",
        "restrict_ip",
        "last_ip",
        "login_after",
        "user_type",
        "last_active",
        "login_before",
        "bypass_restrict_ip_check_if_2fa_enabled",
        "last_login",
        "last_known_versions",
        "api_key",
        "api_secret",
        "onboarding_status",
    ]
    doctype = "User"

    def reset_password(self):
        """
        Reset password of a user
        """
        reset_password_link = self.conn.post_api(
            "parent_portal.api.login.reset_password", {"email": self.email}
        )
        self.reset_password_key = reset_password_link.split("/")[-1]
        return reset_password_link

    def update_password(self, new_password):
        """
        Update password of a user
        """
        if getattr(self, "reset_password_key", None) is None:
            raise Exception("reset_password_key is required to update password")

        return self.conn.post_api(
            "frappe.core.doctype.user.user.update_password",
            {
                "key": self.reset_password_key,
                "new_password": new_password,
            },
        )
