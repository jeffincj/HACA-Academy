class PlacementAI:

    def readiness_score(
        self,
        cgpa,
        skill_count
    ):

        score = min(
            100,
            (cgpa * 8) + (skill_count * 4)
        )

        if score >= 90:
            status = "Excellent"

        elif score >= 70:
            status = "Good"

        else:
            status = "Needs Improvement"

        return score, status