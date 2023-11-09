# MIT License

# Copyright (c) 2020 Hongrui Zheng

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.substitutions import (
    LaunchConfiguration,
    PythonExpression,
    TextSubstitution,
    PathJoinSubstitution,
)
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import (
    IfCondition,
    evaluate_condition_expression,
    LaunchConfigurationEquals,
    LaunchConfigurationNotEquals,
    UnlessCondition,
)
from ament_index_python.packages import get_package_share_directory
import os
import yaml


def generate_launch_description():
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                launch_description_source=PathJoinSubstitution(
                    [FindPackageShare("f1tenth_gym_ros"), "launch", "gym_bridge_launch.py"]
                ),
                launch_arguments={"run_headless": "True"}.items(),
            )
        ]
    )
