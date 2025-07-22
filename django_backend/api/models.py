from django.db import models

# PUBLIC_INTERFACE
class School(models.Model):
    """Represents a school in the system."""
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# PUBLIC_INTERFACE
class Teacher(models.Model):
    """Represents a teacher who can teach one or many classes in a school."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(
        School, 
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# PUBLIC_INTERFACE
class Class(models.Model):
    """Represents a class taught by a teacher at a school, holding students."""
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='classes'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classes'
    )

    def __str__(self):
        return f"{self.name} ({self.school.name})"

# PUBLIC_INTERFACE
class Student(models.Model):
    """Represents a student enrolled in a class at a school."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='students'
    )
    assigned_class = models.ForeignKey(
        Class,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
