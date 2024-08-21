#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "cpp/genetic_algorithm.cpp"

namespace py = pybind11;

PYBIND11_MODULE(genetic_algorithm_cpp, m) {
    py::class_<Robot>(m, "Robot")
        .def(py::init<int>())
        .def("evaluate_fitness", &Robot::evaluate_fitness)
        .def_readwrite("genes", &Robot::genes)
        .def_readwrite("fitness", &Robot::fitness);

    py::class_<GeneticAlgorithm>(m, "GeneticAlgorithm")
        .def(py::init<int, int, int, double>())
        .def("run", &GeneticAlgorithm::run)
        .def("get_best_robot", &GeneticAlgorithm::get_best_robot);
}
