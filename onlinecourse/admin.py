from django.contrib import admin

# Import all 7 models required by the lab
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# ----- Inlines (edit related objects on the same page) -----

# Show lessons inside the Course admin page
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Show questions inside the Course admin page
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Show choices inside the Question admin page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


# ----- Admin classes -----

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'course']
    list_filter = ['course']
    search_fields = ['title', 'content']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'course', 'grade']
    list_filter = ['course']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


# ----- Register models -----

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
