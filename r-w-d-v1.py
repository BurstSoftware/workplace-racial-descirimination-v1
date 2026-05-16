import streamlit as st

st.set_page_config(
    page_title="Workplace Concepts Explorer",
    layout="wide"
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
pages = [
    "Home",
    "Workplace Discrimination Definition",
    "Managerial Misconduct & Accountability",
    "Employee Reporting & Communication Barriers",
    "Workplace Data & Reporting System Inaccuracies",
    "Selective Enforcement of Workplace Rules",
    "HR Consistency & Policy Application",
    "Combined Concept Summary"
]

page = st.sidebar.selectbox("Navigate Concepts", pages)

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":
    st.title("Workplace Concepts Explorer")

    st.write(
        """
        This application organizes workplace-related conceptual definitions
        discussed in this conversation into structured sections.

        Each page represents a different workplace governance or fairness concept,
        including management behavior, reporting systems, and policy enforcement.
        """
    )

# -----------------------------
# Workplace Discrimination
# -----------------------------
elif page == "Workplace Discrimination Definition":
    st.title("Workplace Discrimination (Conceptual Definition)")

    st.write(
        """
        A workplace environment where an individual or group may experience
        differential treatment based on a protected characteristic (such as race),
        resulting in inequitable outcomes in hiring, scheduling, discipline,
        compensation, or working conditions.

        This concept is typically evaluated through patterns of treatment,
        policy application, and workplace impact rather than isolated events.
        """
    )

# -----------------------------
# Managerial Misconduct
# -----------------------------
elif page == "Managerial Misconduct & Accountability":
    st.title("Managerial Misconduct & Accountability")

    st.write(
        """
        A workplace condition where a manager may exercise authority in ways that
        are not properly reviewed or constrained by oversight mechanisms.

        This can include:
        - Failure to consider employee-provided factual information
        - Repeated interruption or dismissal of employee explanations
        - Ignoring operational or health-related context
        - Making unilateral decisions without transparent review

        Lack of accountability structures can amplify the impact of these behaviors.
        """
    )

# -----------------------------
# Communication Barriers
# -----------------------------
elif page == "Employee Reporting & Communication Barriers":
    st.title("Employee Reporting & Communication Barriers")

    st.write(
        """
        A communication dynamic where employees are unable to fully present facts
        or workplace conditions due to interruptions, dismissal, or procedural barriers.

        This may include:
        - Repeated interruption during explanations
        - Preventing completion of factual reporting
        - Dismissal of operational or contextual information
        - Breakdown in structured reporting channels
        """
    )

# -----------------------------
# Data / Reporting Systems
# -----------------------------
elif page == "Workplace Data & Reporting System Inaccuracies":
    st.title("Workplace Data & Reporting System Inaccuracies")

    st.write(
        """
        A condition where workplace performance systems or reporting tools may
        not accurately reflect actual employee output or operational activity.

        This can involve:
        - Mismatches between production output and recorded metrics
        - System errors affecting performance dashboards
        - Discrepancies between operational leadership and reporting systems
        - Misalignment between units produced, hours worked, and error rates
        """
    )

# -----------------------------
# Selective Enforcement
# -----------------------------
elif page == "Selective Enforcement of Workplace Rules":
    st.title("Selective Enforcement of Workplace Rules")

    st.write(
        """
        A workplace condition where policies, rules, or disciplinary standards
        are applied inconsistently across different employees or groups.

        This may involve:
        - Different enforcement levels for similar behaviors
        - Unequal disciplinary actions under the same policy
        - Perceived inconsistencies in rule application across groups
        - Variation in managerial interpretation of standards
        """
    )

# -----------------------------
# HR Consistency
# -----------------------------
elif page == "HR Consistency & Policy Application":
    st.title("HR Consistency & Policy Application")

    st.write(
        """
        A framework describing how human resources policies are applied across a workforce.

        Key elements include:
        - Consistent application of workplace policies
        - Equal review processes for employee concerns
        - Documentation and escalation procedures
        - Ensuring fairness in disciplinary and evaluation systems
        """
    )

# -----------------------------
# Combined Summary
# -----------------------------
elif page == "Combined Concept Summary":
    st.title("Combined Workplace Concept Summary")

    st.write(
        """
        This section combines the discussed concepts into a unified framework:

        - Workplace discrimination (as a general structural concept)
        - Managerial conduct and accountability limitations
        - Communication barriers affecting employee reporting
        - Data/reporting system inaccuracies affecting performance metrics
        - Selective enforcement of workplace rules
        - HR consistency in policy application

        Together, these describe how organizational structure, management behavior,
        and system accuracy can interact to shape employee experience and evaluation outcomes.
        """
    )
