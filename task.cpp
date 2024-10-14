#include <iostream>
#include <future>
#include <chrono>
#include <thread>
#include <functional>
#include <random>

/*
bugs!!!
*/
void task_driver(std::function<void(int)> job, int workload)
{
    std::packaged_task<void(int)> task(job);
    std::future<void> future = task.get_future();
    std::thread taskThread(task, workload);
    std::cout << "Task started\n";
    taskThread.join();
    std::cout << "Task completed\n";
}



int main()
{

    auto job = [](int workload) -> void
    {
        for (int i = workload; i > 0; --i)
        {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_real_distribution<double> dis(0.5, 1.5);
            double sleepTime = dis(gen);
            std::this_thread::sleep_for(std::chrono::duration<double>(sleepTime));
            std::cout << "Completed step #" << i << '\n';
        }
    };

    const int steps = 10;
    task_driver(job, steps);

    return 0;
}