#include "nlohmann/json.hpp"
#include <iostream>

using json = nlohmann::json;

int main()
{
  std::cout << "\n===== BEGIN TestPackage =====\n";

  const json jsonObject = {{"pi", 3.141},
                     {"happy", true},
                     {"name", "Niels"},
                     {"nothing", nullptr},
                     {"answer", {{"everything", 42}}},
                     {"list", {1, 0, 2}},
                     {"object", {{"currency", "USD"}, {"value", 42.99}}}};

  std::cout << std::setw(4) << jsonObject << '\n';

#ifndef NDEBUG
    std::cout << "Build Type: DEBUG\n";
#else
    std::cout << "Build Type: RELEASE\n";
#endif

    std::cout << "====== END TestPackage ======\n";
    return 0;
}
