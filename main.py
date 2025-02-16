#include <stdio.h>
#define MAX_AREAS 100
typedef struct {
int area_id;
int urgency_level;
} Area;
int compare(const void *a, const void *b) {
return ((Area *)a)->urgency_level - ((Area *)b)->urgency_level;
}
void allocateResources(Area areas[], int num_areas, int
num_resources) {
// Sort the areas based on their urgency level
qsort(areas, num_areas, sizeof(Area), compare);
// Allocate resources to the most urgent areas first
printf("Resource allocation:\n");
for (int i = 0; i < num_resources && i < num_areas; i++) {
printf("Allocate resources to area %d with urgency level
%d\n", areas[i].area_id, areas[i].urgency_level);
}
}
int main() {
int num_areas, num_resources;
printf("Enter the number of a

ected areas: ");

scanf("%d", &num_areas);
printf("Enter the number of available resources: ");
scanf("%d", &num_resources);
Area areas[MAX_AREAS];
printf("Enter information about each a

ected area:

\n");
for (int i = 0; i < num_areas; i++) {
printf("Area %d - Urgency level: ", i + 1);
scanf("%d", &areas[i].urgency_level);
areas[i].area_id = i + 1;
}
allocateResources(areas, num_areas, num_resources);
return 0;
}
