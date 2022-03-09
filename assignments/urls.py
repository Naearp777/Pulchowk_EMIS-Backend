from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/assignment/create/<int:c_id>/<int:t_id>/",
        views.create_assignment,
        name="create_assignment",
    ),
    path(
        "api/assignment/submit/<int:a_id>/<int:s_id>/",
        views.submit_assignment,
        name="submit_assignment",
    ),
    path(
        "api/assignment/show/<int:pk>/", views.show_assignment, name="show_assignment"
    ),
    path(
        "api/assignment/show/all/<int:c_id>/", views.show_all_assignment_in_specific_class, name="show_all_assignments_in_specific_class"
    ),
    path("api/assignment/show/assignment/student/<int:a_id>/<int:s_id>/", views.show_assignment_details_of_a_specific_assignment_for_a_student, name="show_assignment_details_of_a_specific_assignment_for_a_student"),
    path(
        "api/assignment/show/all/<int:t_id>/<int:c_id>/",
        views.show_all_assignment_given_by_teacher_in_specific_class,
        name="show_all_assignment_given_by_teacher_in_specific_class",
    ),
    path(
        "api/assignment/show/submitted/<int:a_id>/",
        views.show_submitted_assignments_for_an_assignment,
        name="show_submitted_assignments_for_an_assignment",
    ),
    path(
        "api/assignment/show/all/submitted/<int:s_id>/",
        views.show_all_submitted_assignments_for_a_student,
        name="show_all_submitted_assignments_for_a_student",
    ),
    path(
        "api/assignment/show/all/submitted/<int:s_id>/<int:c_id>/",
        views.show_all_submitted_assignments_for_a_student_in_a_class,
        name="show_all_submitted_assignments_for_a_student_in_a_class",
    ),
    path(
        "api/assignment/update/<int:pk>/",
        views.update_assignment,
        name="update_assignment",
    ),
    path(
        "api/assignment/delete/<int:pk>/",
        views.delete_assignment,
        name="delete_assignment",
    ),
    path(
        "api/assignment/show/postdue/<int:c_id>/",
        views.show_all_post_due_assignments_for_a_student,
        name="show_all_post_due_assignments_for_a_student",
    ),
    path(
        "api/assignment/show/calendar/<int:c_id>/<int:month_id>/<int:year_id>/",
        views.calendar_view_for_student_for_month,
        name="calendar_view_for_student_for_month",
    ),
    path(
        "api/assignment/show/all/class/specific/student/<int:s_id>/",
        views.show_all_assignments_for_all_class_given_to_specific_student,
        name="show_all_assignments_for_all_class_given_to_specific_student",
    ),
    path(
        "api/assignment/show/all/class/specific/student/<int:s_id>/<int:month_id>/<int:year_id>/",
        views.show_all_assignments_for_all_class_given_to_specific_student_in_a_month,
        name="show_all_assignments_for_all_class_given_to_specific_student_for_month",
    ),
    path("api/assignment/submission/mark/<int:a_id>/<int:s_id>/", views.mark_submission_of_a_student_for_an_assignment, name="mark_submission_of_a_student_for_an_assignment")
]
