/**
 * Opera Neon Spatial Workspace — C++ 3D Physics Layout Solver
 * Computes 3D spatial window coordinates, depth parallax, and spring-damper physics
 * for spatial web browser workspaces (VisionOS / WebXR target).
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <memory>

struct Vec3 {
    double x, y, z;
    Vec3 operator+(const Vec3& o) const { return {x + o.x, y + o.y, z + o.z}; }
    Vec3 operator-(const Vec3& o) const { return {x - o.x, y - o.y, z - o.z}; }
    Vec3 operator*(double s) const { return {x * s, y * s, z * s}; }
    double magnitude() const { return std::sqrt(x*x + y*y + z*z); }
    Vec3 normalized() const {
        double m = magnitude();
        return m > 1e-9 ? Vec3{x/m, y/m, z/m} : Vec3{0, 0, 0};
    }
};

struct SpatialWindow {
    uint32_t window_id;
    std::string title;
    Vec3 position;
    Vec3 velocity;
    Vec3 target_position;
    double width;
    double height;
    double depth_scale;    // Parallax scale (1.0 = focused, 0.6 = background)
    double opacity;        // 0.0 to 1.0
    bool is_focused;
    bool is_pinned;
};

class SpringDamperPhysics {
    double stiffness;  // Spring constant k
    double damping;    // Damping coefficient c
    double mass;       // Window virtual mass

public:
    SpringDamperPhysics(double k = 120.0, double c = 18.0, double m = 1.0)
        : stiffness(k), damping(c), mass(m) {}

    Vec3 compute_force(const Vec3& pos, const Vec3& vel, const Vec3& target) const {
        Vec3 displacement = target - pos;
        Vec3 spring_force = displacement * stiffness;
        Vec3 damping_force = vel * (-damping);
        return spring_force + damping_force;
    }

    void step(SpatialWindow& win, double dt_seconds) const {
        if (win.is_pinned) return;

        Vec3 force = compute_force(win.position, win.velocity, win.target_position);
        Vec3 accel = force * (1.0 / mass);
        
        win.velocity = win.velocity + accel * dt_seconds;
        win.position = win.position + win.velocity * dt_seconds;

        // Smooth depth scaling based on Z position
        double target_scale = win.is_focused ? 1.0 : std::max(0.4, 1.0 - (win.position.z / 1000.0));
        win.depth_scale += (target_scale - win.depth_scale) * 0.1;
        win.opacity = std::clamp(1.0 - (win.position.z / 1500.0), 0.2, 1.0);
    }
};

class SpatialLayoutManager {
    std::vector<SpatialWindow> windows;
    SpringDamperPhysics physics;
    uint32_t active_focused_id;

public:
    SpatialLayoutManager() : active_focused_id(0) {}

    void add_window(uint32_t id, const std::string& title, double w, double h) {
        SpatialWindow win;
        win.window_id = id;
        win.title = title;
        win.position = {0, 0, 500}; // Start slightly pushed back
        win.velocity = {0, 0, 0};
        win.target_position = {0, 0, 0};
        win.width = w;
        win.height = h;
        win.depth_scale = 0.8;
        win.opacity = 1.0;
        win.is_focused = false;
        win.is_pinned = false;
        windows.push_back(win);
    }

    void focus_window(uint32_t id) {
        active_focused_id = id;
        int idx = 0;
        for (auto& win : windows) {
            if (win.window_id == id) {
                win.is_focused = true;
                win.target_position = {0, 0, 0}; // Bring to front center
            } else {
                win.is_focused = false;
                // Arrange inactive windows in an arc behind main window
                double angle = (idx - 1.0) * 0.4;
                double radius = 400.0;
                win.target_position = {
                    radius * std::sin(angle),
                    (idx % 2 == 0 ? 50.0 : -50.0),
                    radius * (1.0 - std::cos(angle)) + 200.0
                };
                idx++;
            }
        }
    }

    void update_physics(double dt_seconds) {
        for (auto& win : windows) {
            physics.step(win, dt_seconds);
        }
    }

    const std::vector<SpatialWindow>& get_windows() const { return windows; }

    void print_layout() const {
        std::cout << "=== Spatial Workspace Layout State ===" << std::endl;
        for (const auto& win : windows) {
            std::cout << "Window #" << win.window_id << " [" << win.title << "]"
                      << (win.is_focused ? " (FOCUSED)" : "")
                      << "\n  Pos: (" << win.position.x << ", " << win.position.y << ", " << win.position.z << ")"
                      << "\n  Scale: " << win.depth_scale << " | Opacity: " << win.opacity << "\n";
        }
    }
};

int main() {
    SpatialLayoutManager manager;
    manager.add_window(1, "Main Workspace", 1200, 800);
    manager.add_window(2, "Code Editor", 1000, 700);
    manager.add_window(3, "Terminal Diagnostics", 900, 600);

    manager.focus_window(1);

    // Simulate 60 FPS physics for 0.5s
    for (int frame = 0; frame < 30; frame++) {
        manager.update_physics(1.0 / 60.0);
    }

    manager.print_layout();
    return 0;
}
